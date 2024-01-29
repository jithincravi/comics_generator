import json

from generate_panels import generate_panels
from stability_ai import text_to_image
from add_text import add_text_to_panel
from create_strip import create_strip

# ==========================================================================================

SCENARIO = """
Characters: Superstar is a guy who looks like young Rajnikanth has a moustache and wears a black suit.
New York City is in danger of an alien attack from a round Spaceship. 
Superstar the young Rajnikanth lookalike flies towards the round Alien spaceship with a machete.
Superstar the young Rajnikanth lookalike destroys the round alien spaceship with the machete.
"""

"""SCENARIO = Red balls and Evil Black Squares were always at war wit each other. 
In the end, Red balls win the war after destroying the evil black squares."""

STYLE = "american comic, greyscale"

REGENERATE = []

# ==========================================================================================

print(f"Generate panels with style '{STYLE}' for this scenario: \n {SCENARIO}")
if len(REGENERATE) == 0:
  panels = generate_panels(SCENARIO)

  with open('output/panels.json', 'w') as outfile:
    json.dump(panels, outfile)
else:
  with open('output/panels.json') as json_file:
    panels = json.load(json_file)


from PIL import Image

panel_images = []

for panel in panels:
  if len(REGENERATE) == 0 or int(panel['number']) in REGENERATE:
    panel_prompt = panel["description"] + ", cartoon box, " + STYLE
    print(f"Generate panel {panel['number']} with prompt: {panel_prompt}")
    panel_image = text_to_image(panel_prompt)
    panel_image_with_text = add_text_to_panel(panel["text"], panel_image)
    panel_image_with_text.save(f"output/panel-{panel['number']}.png")
  final_panel = Image.open(f"output/panel-{panel['number']}.png")
  panel_images.append(final_panel)

create_strip(panel_images).save("output/strip.png")
