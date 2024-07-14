from scrapers.myntra_scraper import scrape_myntra_trends
from scrapers.ajio_scraper import scrape_ajio_trends
from social_media.instagram_collector import collect_instagram_posts

if __name__ == "__main__":
    # Scrape from Myntra
    myntra_url = 'https://www.myntra.com/trends'
    myntra_trends = scrape_myntra_trends(myntra_url)
    print("Myntra trends:")
    print(myntra_trends)

    # Scrape from Ajio
    ajio_url = 'https://www.ajio.com/trends'
    ajio_trends = scrape_ajio_trends(ajio_url)
    print("Ajio trends:")
    print(ajio_trends)

    # Collect data from Instagram
    instagram_query = 'fashion trends 2024'
    instagram_posts = collect_instagram_posts(instagram_query)
    print("Instagram posts:")
    print(instagram_posts)

    # Combine all data
    all_trends = myntra_trends + ajio_trends + instagram_posts
    print("All collected trends:")
    print(all_trends)
