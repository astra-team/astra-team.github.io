---
title: Info
date: 2022-10-24

type: landing

sections:
  - block: markdown
    content:
      title: Info
      text: |
        Directors: Fawzi Nashashibi (Inria) and Benazouz Bradai (Valeo)

  - block: contact
    content:
      # title: 
      # text: |-
      #   Lorem ipsum dolor sit amet, consectetur adipiscing elit. Integer tempus augue non tempor egestas. Proin nisl nunc, dignissim in accumsan dapibus, auctor ullamcorper neque. Quisque at elit felis. Vestibulum ante ipsum primis in faucibus orci luctus et ultrices posuere cubilia curae; Aenean eget elementum odio. Cras interdum eget risus sit amet aliquet. In volutpat, nisl ut fringilla dignissim, arcu nisl suscipit ante, at accumsan sapien nisl eu eros.
      # email: test@example.org
      # phone: 888 888 88 88
      address:
        street: 2 rue Simone Iff
        city: Paris
        # region: CA
        postcode: '75012'
        country: France
        country_code: FR
      coordinates:
        latitude: '48.8414531'
        longitude: '2.3846535'
      directions: 1st floor Building A. You need to go to reception in Building C to get access.
      # office_hours:
      #   - 'Monday 10:00 to 13:00'
      #   - 'Wednesday 09:00 to 10:00'
      # appointment_url: 'https://calendly.com'
      #contact_links:
      #  - icon: comments
      #    icon_pack: fas
      #    name: Discuss on Forum
      #    link: 'https://discourse.gohugo.io'
    
      # Automatically link email and phone or display as text?
      autolink: true
    
      # Email form provider
      # form:
      #   provider: netlify
      #   formspree:
      #     id:
      #   netlify:
      #     # Enable CAPTCHA challenge to reduce spam?
      #     captcha: false
    design:
      columns: '1'
  - block: markdown
    content:
      title:
      subtitle: ''
      text:
    design:
      columns: '1'
      background:
        image: 
          filename: inria.jpg
          filters:
            brightness: 1
          parallax: true
          position: center
          size: cover
          text_color_light: true
      spacing:
        padding: ['20px', '0', '20px', '0']
      css_class: fullscreen
---
