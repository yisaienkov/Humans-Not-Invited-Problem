"""
Main Inference.
"""
import asyncio

from humans_not_invited_problem import get_correct_images_by_content


if __name__ == "__main__":
    print("Input content of the html page (finish you input with 'END'):")
    content = ""
    while True:
        tmp = input().replace("&amp;", "&")
        if tmp == "END":
            break
        content += tmp
    
    print("Processing...")

    loop = asyncio.get_event_loop()
    loop.run_until_complete(get_correct_images_by_content(content))
    loop.close()