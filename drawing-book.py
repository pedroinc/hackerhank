#!/bin/python3

import sys


def solve(number_of_pages, wanted_page):

    start_from_the_end = False
    page_groups = []

    if number_of_pages - wanted_page < wanted_page:
        start_from_the_end = True

    if wanted_page == 1 or wanted_page == number_of_pages:
        return 0
    else:
        page_groups.append(1)
        for x in range(2, number_of_pages, 2):
            page_groups.append((x, x + 1))
        if number_of_pages % 2 == 0:
            page_groups.append(number_of_pages)

        turned_pages = 0

        if start_from_the_end:
            for m_tuple in reversed(page_groups):
                if type(m_tuple) == tuple and wanted_page in m_tuple:
                    return turned_pages
                else:
                    turned_pages = turned_pages + 1
        else:
            for m_tuple in page_groups:
                if type(m_tuple) == tuple and wanted_page in m_tuple:
                    return turned_pages
                else:
                    turned_pages = turned_pages + 1


n = int(input().strip())
p = int(input().strip())
result = solve(n, p)
print(result)
