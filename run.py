# import utilities
from utilities.scrape_repo import get_top_repo_urls, get_top_repos, get_top_contributors, remove_duplicates_in_csv
from utilities.scrape_user import get_top_user_urls, get_top_users

if __name__ == '__main__':
    save_directory = "result"     # The base directory where the result will be stored
    keyword = "next.js"          # The keyword for search
    start_page = 1                # Start of pagination
    stop_page = 1000            # The last page in pagination
    # Get the information of only contributors or to get the information of both contributors
    get_user_info_only = False
    max_n_top_contributors = 1000  # The maximum contributor of the repo
    sort_by = "best_match"        # Sort by best match

    get_top_contributors(
        keyword,
        sort_by=sort_by,
        max_n_top_contributors=max_n_top_contributors,
        start_page=start_page,
        stop_page=stop_page,
        get_user_info_only=get_user_info_only,
        save_directory=save_directory
    )

    remove_duplicates_in_csv(
        keyword=keyword,
        sort_by=sort_by,
        start_page=start_page,
        stop_page=stop_page,
        save_directory=save_directory
    )
    # get_top_users(keyword, stop_page=stop_page, save_directory=save_directory)
