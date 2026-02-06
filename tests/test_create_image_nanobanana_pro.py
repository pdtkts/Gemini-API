"""
Test script for chat with image - redraw in milk tea style.
"""

import asyncio
import os
from pathlib import Path

from gemini_webapi import GeminiClient, ImageMode, set_log_level
from gemini_webapi.constants import Model

# Load .env from project root
env_path = Path(__file__).parent.parent / ".env"
if env_path.exists():
    with open(env_path) as f:
        for line in f:
            line = line.strip()
            if line and not line.startswith("#") and "=" in line:
                key, _, value = line.partition("=")
                value = value.strip().strip('"').strip("'")
                os.environ.setdefault(key.strip(), value)

set_log_level("DEBUG")

# Get credentials from environment
Secure_1PSID = os.getenv("SECURE_1PSID", "")
Secure_1PSIDTS = os.getenv("SECURE_1PSIDTS", "")


async def main():
    """Send image and request redraw in milk tea style."""
    client = GeminiClient(Secure_1PSID, Secure_1PSIDTS, proxy=None)
    await client.init(timeout=300,auto_close=False, close_delay=300, auto_refresh=True)

    # Read prompt from file
    prompt_file = Path(__file__).parent / "test_prompt.txt"
    prompt = prompt_file.read_text(encoding="utf-8").strip() if prompt_file.exists() else "Generate an image"

    # Send image with prompt to redraw using Nano Banana Pro
    response = await client.generate_content(
        prompt,
        # files=[Path("temp/1.jpg")],
        model=Model.G_3_0_PRO,
        image_mode=ImageMode.PRO,
    )
    print(f"Response: {response.text}")

    # Save generated images if any
    if response.images:
        print(f"Generated {len(response.images)} image(s)")
        for idx, image in enumerate(response.images):
            print(f"Image {idx + 1}: {image}")
            await image.save(verbose=True, full_size=True)
    else:
        print("No images generated")


if __name__ == "__main__":
    asyncio.run(main())
