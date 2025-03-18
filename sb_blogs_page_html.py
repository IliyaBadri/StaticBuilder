import urllib.parse
import main
import traceback
import sys
import os
import urllib
import shutil
import datetime

def create_blogs_html(blogs_config_path:str, manifest_config_data: dict, site_config_data: dict, blogs_page_config_data: dict, blogs_config_data: dict):
    try:
        blogs_directory = os.path.abspath(os.path.join(main.EXPORT_DIRECTORY, "blogs"))
        blogs_path = os.path.join(blogs_directory, "blogs.json")

        blogs_html_path = os.path.abspath(os.path.join(main.EXPORT_DIRECTORY, "blogs/index.html"))

        print(f"[+] Creating {blogs_path}")
        os.makedirs(blogs_directory, exist_ok=True)
        shutil.copy(blogs_config_path, blogs_path)

        print(f"[+] Creating {blogs_html_path}")

        three_newest_blogs = ""
        newest_blog_count = 0

        for blog_data in blogs_config_data["blogs"]:
          if newest_blog_count >= 3:
            break
          three_newest_blogs += f"""<li><a href="{blog_data["path"]}" class="text-purple-500 hover:underline">{blog_data["title"]}</a></li>
            """
          newest_blog_count += 1
            
        with open(blogs_html_path, "w") as blogs_html_file:
            contents = f"""<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <meta name="theme-color" content="{manifest_config_data["theme_color"]}">
  <meta name="description" content="{blogs_page_config_data["blogs_description"]}">

  <meta property="og:title" content="Blogs - {manifest_config_data["short_name"]}">
  <meta property="og:description" content="{blogs_page_config_data["blogs_description"]}">
  <meta property="og:image" content="{urllib.parse.urljoin(f"https://{site_config_data["domain"]}/", "/images/favicon.png")}">
  <meta property="og:url" content="https://{site_config_data["domain"]}/blogs">
  <meta property="og:type" content="website">

  <meta name="twitter:card" content="summary_large_image">
  <meta name="twitter:title" content="Blogs - {manifest_config_data["short_name"]}">
  <meta name="twitter:description" content="{blogs_page_config_data["blogs_description"]}">
  <meta name="twitter:image" content="{urllib.parse.urljoin(f"https://{site_config_data["domain"]}/", "/images/favicon.png")}">

  <link rel="shortcut icon" href="/images/favicon.png" type="image/png">
  <link rel="manifest" href="/json/manifest.json">
  <link href="/css/tailwind.css" rel="stylesheet">
  <title>Blogs - {manifest_config_data["short_name"]}</title>
</head>
<body class="bg-white text-gray-800">
  <nav class="w-full fixed top-0 left-0 bg-white shadow-md p-4 flex justify-between items-center mx-auto">
    <button onclick="window.location.href='/'" class="text-xl font-semibold">{manifest_config_data["name"]}</button>
    <div class="space-x-4">
      <button onclick="window.location.href='/about/'" class="px-4 py-2 bg-gray-200 rounded-lg hover:bg-gray-300">{blogs_page_config_data["about_navbar_button_text"]}</button>
      <button onclick="window.location.href='/blogs/'" class="px-4 py-2 bg-gray-200 rounded-lg hover:bg-gray-300">{blogs_page_config_data["blogs_navbar_button_text"]}</button>
    </div>
  </nav>
  <div class="flex flex-col lg:flex-row p-8 pt-24 mt-20">
    <div class="lg:w-2/3 space-y-8">
      <div class="bg-white p-1 rounded-xl shadow-xl border-2 border-gray-200 flex flex-row items-center">
        <input id="search-input" class="inset-ring-purple-900 rounded-2xl border-2 p-2 mr-1 w-full" placeholder="{blogs_page_config_data["search_placeholder"]}"/>
        <button id="search-button" class="px-6 py-2 bg-green-600 text-white rounded-lg hover:bg-gray-700 transition duration-300">{blogs_page_config_data["search_button_text"]}</button>
      </div>
      <div id="blog-container" class="space-y-8">
      </div>
    </div>
    <div class="lg:w-1/3 mt-8 lg:mt-0 lg:ml-8">
        <div class="bg-gray-100 p-6 rounded-lg shadow-lg">
            <h3 class="text-xl font-semibold text-gray-800">{blogs_page_config_data["about_me_section_title"]}</h3>
            <p class="text-gray-600 mt-4">{blogs_page_config_data["about_me_section_description"]}</p>
            <button onclick="window.location.href='/about'" class="mt-4 px-6 py-2 bg-gray-800 text-white rounded-lg hover:bg-gray-700 transition duration-300">{blogs_page_config_data["about_me_section_button_text"]}</button>
        </div>
        <div class="mt-8 bg-gray-100 p-6 rounded-lg shadow-lg">
            <h3 class="text-xl font-semibold text-gray-800">{blogs_page_config_data["latest_post_section_title"]}</h3>
            <ul class="space-y-2 mt-4">
            {three_newest_blogs}
            </ul>
        </div>
    </div>
    </div>
  <footer class="bg-gray-800 text-white text-center py-6 mt-8">
    <p>&copy; {datetime.datetime.now().year} {manifest_config_data["name"]}. All rights reserved.</p>
  </footer>
<script>
let jsonData = null;
let selectedBlogs = [];
let searchQuery = "";
let searchButton = document.getElementById("search-button");
let searchInput = document.getElementById("search-input");
let blogContainer = document.getElementById("blog-container");

main();

async function main(){{
  await fetchJsonData();
  reloadBlogs();
}}

searchButton.addEventListener("click", async() => {{
  searchQuery = searchInput.value;
  reloadBlogs();
}});

async function fetchJsonData() {{
  try {{
  const response = await fetch("/blogs/blogs.json");

    if (!response.ok) {{
      throw new Error("Couldn't fetch json data.");
    }}
    jsonData = await response.json();
  }} catch (error) {{
    console.error('Error fetching JSON:', error);
    jsonData = null;
  }}
}}

async function reloadBlogs() {{
  selectedBlogs.length = 0;
  const sortedBlogs = searchAndSortItems(jsonData.blogs, searchQuery)
  selectedBlogs.push(...sortedBlogs);

  blogContainer.innerHTML = "";

  for(const blogData of selectedBlogs){{
    const blogCardDiv = document.createElement('div');
    blogCardDiv.className = 'bg-white p-6 rounded-xl shadow-xl border-2 border-gray-200';

    const blogTitleH2 = document.createElement('h2');
    blogTitleH2.className = 'text-2xl font-semibold text-gray-800';
    blogTitleH2.innerText = blogData.title;

    const blogDescriptionP = document.createElement('p');
    blogDescriptionP.className = 'text-gray-600 mt-4';
    blogDescriptionP.innerText = blogData.description;

    const blogReadMoreButton = document.createElement('button');
    blogReadMoreButton.className = 'mt-4 px-6 py-2 bg-gray-800 text-white rounded-lg hover:bg-gray-700 transition duration-300';
    blogReadMoreButton.innerText = 'Read More';
    blogReadMoreButton.addEventListener("click", () => {{
      window.location.href = blogData.path;
    }});

    blogCardDiv.appendChild(blogTitleH2);
    blogCardDiv.appendChild(blogDescriptionP);
    blogCardDiv.appendChild(blogReadMoreButton);

    blogContainer.appendChild(blogCardDiv);
  }}
}}

function searchAndSortItems(items, searchString) {{
  if (!searchString) {{
    return items;
  }}

  const normalizedSearchString = searchString.toLowerCase();

  return items.filter(item => {{
    const normalizedTitle = item.title.toLowerCase();
    const normalizedDescription = item.description.toLowerCase();

    return normalizedTitle.includes(normalizedSearchString) ||
           normalizedDescription.includes(normalizedSearchString);
  }}).sort((a, b) => {{

      const aTitleIndex = a.title.toLowerCase().indexOf(normalizedSearchString);
      const bTitleIndex = b.title.toLowerCase().indexOf(normalizedSearchString);
      const aDescIndex = a.description.toLowerCase().indexOf(normalizedSearchString);
      const bDescIndex = b.description.toLowerCase().indexOf(normalizedSearchString);

      if (aTitleIndex !== -1 && bTitleIndex !== -1) {{
          return aTitleIndex - bTitleIndex; 
      }} else if (aTitleIndex !== -1 && bTitleIndex === -1 && bDescIndex === -1) {{
          return -1;
      }} else if (aTitleIndex === -1 && bTitleIndex !== -1 && aDescIndex === -1) {{
          return 1;
      }} else if(aDescIndex !== -1 && bDescIndex !== -1){{
        return aDescIndex - bDescIndex;
      }} else if(aDescIndex !== -1 && bDescIndex === -1 && bTitleIndex === -1){{
        return -1;
      }} else if (aDescIndex === -1 && bDescIndex !== -1 && aTitleIndex === -1){{
        return 1;
      }} else {{
        return 0;
      }}
  }});
}}
</script>
</body>
</html>
"""
            blogs_html_file.write(contents)
    except Exception as exception:
        print(f"[-] Error creating {blogs_html_path} or {blogs_path}")
        traceback.print_exc()
        sys.exit(1)