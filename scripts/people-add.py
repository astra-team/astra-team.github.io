import os, re, sys
import numpy as np
import urllib.request
from serpapi import GoogleSearch
import matplotlib.pyplot as plt
import PIL.Image as Image
import avatarwrap

plt.ioff()

peoples = []

members = "Alexandre BOULCH, Researcher, Permanents\n"
members += "Amina GHOUL, PhD Student, Students\n"
members += "Andrei BURSUC, Researcher, Permanents\n"
members += "Anh Quan CAO, PhD Student, Students\n"
members += "Anne MATHURIN, Team assistant, Staff\n"
members += "Axel JEANNE, Research Engineer, Permanents\n"
members += "Gilles Puy, Researcher, Permanents\n"
members += "Benazouz BRADAI, Head of the team, Permanents\n"
members += "Clotilde MONNET, Project Manager, Staff\n"
members += "Fawzi NASHASHIBI, Head of the team, Permanents\n"
members += "Fernando GARRIDO CARPIO, Research Engineer, Permanents\n"
members += "Gérard LE LANN, Researcher Emeritus, Emeriti\n"
members += "Guy FAYOLLE, Researcher Emeritus, Emeriti\n"
members += "Ivan LOPES, PhD Student, Students\n"
members += "Jean-Marc LASGOUTTES, Researcher, Permanents\n"
members += "Jiahao ZHANG, PhD Student, Students\n"
members += "Karim ESSALMI, PhD Student, Students\n"
members += "Mohammad FAHES, PhD Student, Students\n"
members += "Nelson DE MOURA, Post Doc, PostDocs\n"
members += "Noël NADAL, PhD Student, Students\n"
members += "Patrick PÉREZ, Researcher, Permanents\n"
members += "Paulo RESENDE, Research Engineer, Permanents\n"
members += "Raoul DE CHARETTE, Researcher, Permanents\n"
members += "Renaud MARLET, Researcher, Permanents\n"
members += "Souhaiel BEN SALEM, Intern, Students\n"
members += "Tan Khiem HUYNH, Intern, Students\n"
members += "Tetiana Martyniuk, PhD Student, Students\n"
members += "Tuan Hung VU, Researcher, Permanents\n"
members += "Zayed ALSAYED, Research Engineer, Permanents\n"
members += "Fabio Pizzati, Now at Oxford Uni, Alumni\n"
members += "Anne-Verroust Blondet, Retired, Alumni\n"

valid_groups = ["Staff", "Permanents", "Emeriti", "PostDocs", "Engineers", "Students", "Visitors", "Alumni"]
print(
  "*** This script is to automatize addition or edition of a team member. It will (try) extract automatically website and pictures for each member with interactive request. ***\n"
  "Each line should be one person, in the form of:\n"
  "firstname, lastname, role, group\n"
  "\n\n"
  "groups should be within '|': "+"|".join(valid_groups)
)

# members = input("List of members to edit/add:\n")
# members = "Jean-Marc Lasgouttes, Researcher, Permanents\n"
# members += "Andrei Bursuc, Researcher, Permanents\n"
# members += "Raoul DE CHARETTE, Researcher, Permanents\n"
# members += "Alexandre BOULCH , Researcher, PostDocs\n"
members = members.split("\n")

avatar_search = False
post_members = []
for i, member in enumerate(members):
    print("Line #{0}/{1}".format(i, len(members)))
    member = member.strip()
    if len(member) == 0:
        print("   empty, skipping")
        continue

    fullname, role, groups = member.split(',')
    # If lastname is ALL CAPS
    v = re.search(" [A-Z \-']{2,}$", fullname)
    if v is not None:
        surname = v[0]
        name = fullname[:-len(surname)]
    else:
        name, surname = fullname.rsplit(" ", 1)

    name = str(np.char.title(name)).strip()
    surname = str(np.char.title(surname)).strip()

    if surname[:3] == "De ":
        surname = "de "+surname[3:]

    role = role.strip()
    groups = groups.strip().split('|')
    for r in groups:
        if r not in valid_groups:
            print("Group '%s' is invalid. Groups must be among: " % (r)+"|".join(valid_groups))
            assert(False)

    print("   name: %s" % (name))
    print("   surname: %s" % (surname))
    print("   role: %s" % (role))
    print("   groups: %s" % (groups))
    post_members.append({
      "name": name,
      "surname": surname,
      "role": role,
      "groups": groups
    })

def member_create(member, avatar_force=False):
    print("member_create()")
    print(member)
    fullname = member["name"].title()+" "+member["surname"].title()
    fullname_enc = fullname.replace(" ", "-").lower()
    author = fullname_enc
    path = os.path.join(os.pardir, 'content', 'authors', fullname_enc)

    print(path)
    if os.path.exists(path):
        print("Member exists")
        return

    print("New member")

    groups = []
    is_alumni = False
    for g in member["groups"]:
      if g == "Alumni":
        is_alumni = True

    if is_alumni:
        groups.append("Alumni")
    else:
        for g in member["groups"]:
          groups.append(g)

    md_file = "---\n"
    md_file += "_build:\n"
    md_file += "  render: never\n"
    md_file += "cascade:\n"
    md_file += "  _build:\n"
    md_file += "    render: never\n"
    md_file += "    list: always\n"
    md_file += "\n"
    md_file += "# Display name\n"
    md_file += "title: "+fullname+"\n"
    md_file += "\n"
    md_file += "# Full name (for SEO)\n"
    md_file += "first_name: "+member["name"]+"\n"
    md_file += "last_name: "+member["surname"]+"\n"
    md_file += "\n"
    md_file += "# Username (this should match the folder name)\n"
    md_file += "authors:\n"
    md_file += "  - "+author+"\n"
    md_file += "\n"
    md_file += "\n"
    md_file += "# Is this the primary user of the site?\n"
    md_file += "superuser: false\n"
    md_file += "external_link: "+""+"\n"
    md_file += "\n"
    md_file += "# Role/position\n"
    md_file += "role: "+member["role"]+"\n"
    md_file += "\n"
    md_file += "# Organizational groups that you belong to (for People widget)\n"
    md_file += "#   Set this to `[]` or comment out if you are not using People widget.\n"
    md_file += "user_groups:\n"
    for g in groups:
        md_file += "  - "+g+"\n"
    md_file += "---\n"

    # Create folder
    os.makedirs(path, exist_ok=True)
    # Create markdown
    f = open(os.path.join(path, 'index.md'), "w")
    f.write(md_file)
    f.close()

    if avatar_search:
        if avatar_force or not os.path.exists(os.path.join(path, 'avatar.jpg')):
            member_avatar_auto(member)
def remove_transparency(im, bg_colour=(255, 255, 255)):
  # Only process if image has transparency (http://stackoverflow.com/a/1963146)
  if im.mode in ('RGBA', 'LA') or (im.mode == 'P' and 'transparency' in im.info):
    # Need to convert to RGBA if LA format due to a bug in PIL (http://stackoverflow.com/a/1963146)
    alpha = im.convert('RGBA').split()[-1]

    # Create a new background image of our matt color.
    # Must be RGBA because paste requires both images have the same format
    # (http://stackoverflow.com/a/8720632  and  http://stackoverflow.com/a/9459208)
    bg = Image.new("RGBA", im.size, bg_colour + (255,))
    bg.paste(im, mask=alpha)
    return bg.convert('RGB')
  else:
    return im

def member_avatar_save(member, im):
    fullname = member["name"].title()+" "+member["surname"].title()
    fullname_enc = fullname.replace(" ", "-").lower()
    author = fullname_enc
    path = os.path.join(os.pardir, 'content', 'authors', fullname_enc)

    avatar_path = os.path.join(path, "avatar.jpg")
    print(" Saving avatar: %s" % avatar_path)
    if os.path.exists(avatar_path):
        os.remove(avatar_path)

    if im is not None:
        remove_transparency(im).save(avatar_path, 'JPEG', quality=95)

    print("member_avatar_save > done")

def member_avatar_auto(member):
    fullname = member["name"].title()+" "+member["surname"].title()
    print("Finding avatar for: "+fullname)

    ims = avatarwrap.find_images(fullname, num=1)
    member_avatar_save(member, ims[0])
    # member_avatar_save(member, None)


for m in post_members:
    member_create(m, avatar_force=False)
