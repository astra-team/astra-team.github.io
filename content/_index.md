---
# Leave the homepage title empty to use the site title
title:
date: 2022-10-24
type: landing

sections:
  - block: hero
    content:
      title: |
        Astra research team
      image:
        filename: autonomous-visu.jpg
      text: |
        ### Automated and Safe TRAnsportation systems
        We are a joint Inria-Valeo research team hosted at [Inria Paris](https://www.inria.fr/fr/centre-inria-de-paris). We research multiple aspects of intelligent and autonomous transportation from the ego car to the large scale modeling. Our research axes span [Vision and 3D Scene Understanding]({{< relref "/research#vision" >}}), [Localization & Mapping]({{< relref "/research#localization" >}}), [Decision & Motion planning]({{< relref "/research#decision" >}}), [Large scale modeling]({{< relref "/research#modeling" >}}).
  - block: collection
    content:
      title: Latest News
      subtitle:
      text:
      count: 5
      filters:
        author: ''
        category: ''
        exclude_featured: false
        publication_type: ''
        tag: ''
      offset: 0
      order: desc
      page_type: post
    design:
      view: compact
      columns: '2'
    archive:
      enable: true
      text: See all blog posts
      link: post/

  
  # - block: markdown
  #   content:
  #     title:
  #     subtitle: ''
  #     text:
  #   design:
  #     columns: '1'
  #     background:
  #       image: 
  #         filename: coders.jpg
  #         filters:
  #           brightness: 1
  #         parallax: false
  #         position: center
  #         size: cover
  #         text_color_light: true
  #     spacing:
  #       padding: ['20px', '0', '20px', '0']
  #     css_class: fullscreen
  
  - block: markdown
    content:
      title:
      subtitle:
      text: |
        {{% cta cta_link="./people/" cta_text="Meet the team →" %}}
    design:
      columns: '1'
---