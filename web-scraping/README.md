# Community Wikis and Web Scraping Homework

## Wiki Choice and Research Question

For this assignment, I chose the [Minecraft Wiki](https://minecraft.wiki/), a community-run wiki about Minecraft.

My research question is:

**How does the Minecraft Wiki describe a small sample of different Minecraft mobs?**

I chose this wiki because Minecraft contains many different mobs with different behaviors and roles. The descriptions on the wiki could be useful for researchers interested in how game communities organize and describe game objects.

## robots.txt and Scraping Policy

Before scraping, I checked the Minecraft Wiki's robots.txt file:

https://minecraft.wiki/robots.txt

The robots.txt file was accessible and returned a status code of 200. It restricts several special namespaces and technical routes, including pages related to User, Special, File, API, and REST paths. The normal article pages used in this assignment, such as the Mobs page and individual mob pages, were not among the restricted paths I used.

My scraper also uses an identifiable User-Agent and pauses between requests with `time.sleep(1)` to avoid sending requests too quickly.

## Scraping Process

The scraper is stored in `wiki_scraping.py` and uses Python's `requests` and `BeautifulSoup` libraries.

The scraper works in two levels:

1. It requests the main Minecraft Wiki `Mobs` page and finds links for ten selected mobs.
2. It visits each individual mob page and extracts the first substantial descriptive paragraph.

The ten mobs collected are:

- Creeper
- Pig
- Skeleton
- Zombie
- Spider
- Sheep
- Cow
- Chicken
- Slime
- Ghast

## Output Data

The resulting data is stored in `minecraft_mobs.csv`.

The CSV contains three fields:

- `mob_name` — the name of the mob
- `page_url` — the Minecraft Wiki page used as the source
- `description` — the first substantial descriptive paragraph from the page

The current dataset contains 10 records.

## Reflection

This dataset does not directly measure the complete characteristics of Minecraft mobs. Instead, it measures how the Minecraft Wiki describes these mobs in the first substantial paragraph of each article.

The descriptions can contain information about behavior, hostility, habitat, drops, and other characteristics, but these are written in natural language rather than standardized categories. Therefore, the description is a proxy for how each mob is represented on the wiki, not a complete measurement of the mob itself.

Someone could incorrectly conclude that information not mentioned in the first paragraph does not exist or is unimportant. Important details may appear later in the article, and different pages may emphasize different types of information.

Another limitation is that I manually selected ten mobs rather than scraping every mob on the wiki. The sample therefore demonstrates the scraping process but should not be treated as representative of all Minecraft mobs.

## Files

- `wiki_scraping.py` — Python web scraper
- `minecraft_mobs.csv` — scraped structured data
- `README.md` — documentation and reflection
