---
title: Research
date: 2022-10-24

type: landing

sections:
  - block: markdown
    id: section-1
    content:
      title: Research axes
      text: Our research combine mathematics, algorithmics and machine learning to investigate various aspects of intelligent transportation systems, with an emphasis on autonomous driving.
    design:
      # Choose how many columns the section has. Valid values: '1' or '2'.
      columns: '1'
  - block: markdown
    id: vision
    content:
      title: Vision and 3D Perception for Scene Understanding
      # subtitle: A subtitle
      text: |
        We study 2D vision and 3D perception for robust scene understanding. Our research focuses on relaxing the use of abundant data and supervision, stepping towards weak-/un-supervised vision algorithms, while providing models that are more interpretable. We primarily address autonomous driving but our research expands to a variety of indoor and outdoor applications. 
    # [More info](https://astra-vision.github.io/)
    design:
        # Choose how many columns the section has. Valid values: '1' or '2'.
        columns: '2'
  - block: markdown
    id: localization
    content:
      title: Localization & Mapping
      # subtitle: A subtitle
      text: Vehicle localization and environmental mapping are pillars of the perception task for an autonomous vehicle. While vehicle localization ensures the global positioning of the vehicle in its environment and local positioning with regard to the road and to the close road features, environment mapping contributes in building a useful internal representation that is exploited by the decision system. We address here some of the remaining locks about integrity, safety, data size and costs points.
    design:
        # Choose how many columns the section has. Valid values: '1' or '2'.
        columns: '2'
  - block: markdown
    id: decision
    content:
      title: Decision making, motion Planning \& vehicle Control
      # subtitle: A subtitle
      text: Decision-making, maneuver and motion planning, and vehicle control are vital components because they bridge the perception subsystem of the environment and the bottom-level control subsystem. In this axis, we address these issues covering various strategies of designing the decision-making, trajectory planning, and tracking control, as well as shared driving of the human-automation to adapt to different levels of the automated driving system accounting with the driver profile.
    design:
        # Choose how many columns the section has. Valid values: '1' or '2'.
        columns: '2'
  - block: markdown
    id: modeling
    content:
      title: Large scale modeling and deployment of mobility systems in Smart Cities
      # subtitle: A subtitle
      text: This axis is concerned with the use of vehicles, rather with their conception. The focus here is to model systems comprising a large number of vehicles, often seen as random entities. Our methodology explores the links between large random systems and statistical physics -- a powerful approach, both for macroscopic and microscopic analysis. The general setting is mathematical modelling of large systems, without any a priori restriction like networks, random graphs, etc.
    design:
        # Choose how many columns the section has. Valid values: '1' or '2'.
        columns: '2'
  - block: slider
    content:
      slides:
      - title: 🚗 Astra 🧠
        content: Automated and Safe TRAnsportation systems
        align: center
        background:
          image:
            filename: autonomous-visu.jpg
            filters:
              brightness: 0.7
          position: right
          color: '#666'
      - title: Inria Paris
        content: "Astra research team is hosted at Inria Paris, in the historical Paris center."
        align: left
        background:
          image:
            filename: inria.jpg
            filters:
              brightness: 0.7
          position: center
          color: '#555'
        link:
          icon: location-dot
          icon_pack: fas
          text: We're here
          url: ../info/
      - title: RITS fleet
        content: 'Astra succeeded to the Inria RITS team (2012-2022) which had a fleet of autonomous vehicles, including the iconic [Cyber Cab](https://www.youtube.com/watch?v=BdAtKsmXdZU)'
        align: right
        background:
          image:
            filename: rits_fleet.jpg
            filters:
              brightness: 0.5
          position: center
          color: '#333'
        # link:
        #   icon: graduation-cap
        #   icon_pack: fas
        #   text: Join Us
        #   url: ../contact/
    design:
      # Slide height is automatic unless you force a specific height (e.g. '400px')
      slide_height: ''
      is_fullscreen: true
      # Automatically transition through slides?
      loop: false
      # Duration of transition between slides (in ms)
      interval: 2000
---
