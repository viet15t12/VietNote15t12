"""MkDocs hook: isolate course navigation and footer links.

Rules:
1. Only docs/index.md can navigate between courses.
2. Inside a course (e.g. lpic/, ccna/, aws/, ptit/):
   - Sidebar only shows that course and a link back to Home (← Trang chủ).
   - Footer next/previous links NEVER cross course boundaries.
   - Course index pages do not link 'previous' to another course or Home.
   - Course last pages do not link 'next' to another course.
"""

from mkdocs.structure.nav import Link


class ScopedNav:
    """Wrapper around MkDocs Navigation to restrict visible items per page."""

    def __init__(self, original_nav, items):
        self._orig = original_nav
        self.items = items
        self.homepage = original_nav.homepage
        self.pages = original_nav.pages

    def __iter__(self):
        return iter(self.items)

    def __getattr__(self, name):
        return getattr(self._orig, name)


def on_nav(nav, config, files):
    """Isolate previous_page and next_page so they never cross course boundaries."""
    # Group pages by top-level section directory
    course_map = {}
    for p in nav.pages:
        src = p.file.src_uri
        parts = src.split("/")
        course_name = parts[0] if len(parts) > 1 else "_root_"
        course_map.setdefault(course_name, []).append(p)

    for course_name, pages in course_map.items():
        if course_name == "_root_":
            for p in pages:
                p.previous_page = None
                p.next_page = None
        else:
            for i, p in enumerate(pages):
                p.previous_page = pages[i - 1] if i > 0 else None
                p.next_page = pages[i + 1] if i < len(pages) - 1 else None

    return nav


def on_page_context(context, page, config, nav):
    """Scope sidebar navigation to only the current course and Home link."""
    src = page.file.src_uri
    parts = src.split("/")

    # If it is the home page, leave it as is (index.md has hide: [navigation])
    if len(parts) <= 1:
        return context

    current_course_dir = parts[0]

    # Find the matching top section in nav.items
    matching_section = None
    for item in nav.items:
        # Check if item has children or pages in this course directory
        item_pages = getattr(item, "pages", None) or []
        item_children = getattr(item, "children", None) or []

        def belongs_to_course(obj):
            if hasattr(obj, "file") and getattr(obj.file, "src_uri", "").startswith(
                current_course_dir + "/"
            ):
                return True
            for child in getattr(obj, "children", None) or []:
                if belongs_to_course(child):
                    return True
            return False

        if belongs_to_course(item):
            matching_section = item
            break

    if matching_section is not None:
        home_link = Link(title="← Trang chủ", url="")
        scoped = ScopedNav(nav, [home_link, matching_section])
        context["nav"] = scoped

    return context

