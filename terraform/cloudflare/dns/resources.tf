resource "cloudflare_record" "tfer--AAAA_geraldri-002E-ch_590ce12a12ec5913fe301f3d9bea980b" {
  name    = "geraldri.ch"
  proxied = "true"
  ttl     = "1"
  type    = "AAAA"
  value   = "2606:50c0:8002::153"
  zone_id = "7d19aa4b3fa8b5bc91531ec6c6f80ec5"
}

resource "cloudflare_record" "tfer--AAAA_geraldri-002E-ch_ab10c0596ce635e9d68865f3a4154e97" {
  name    = "geraldri.ch"
  proxied = "true"
  ttl     = "1"
  type    = "AAAA"
  value   = "2606:50c0:8000::153"
  zone_id = "7d19aa4b3fa8b5bc91531ec6c6f80ec5"
}

resource "cloudflare_record" "tfer--AAAA_geraldri-002E-ch_bcf56188cfbe2f14dc67706a7f6eaff8" {
  name    = "geraldri.ch"
  proxied = "true"
  ttl     = "1"
  type    = "AAAA"
  value   = "2606:50c0:8003::153"
  zone_id = "7d19aa4b3fa8b5bc91531ec6c6f80ec5"
}

resource "cloudflare_record" "tfer--AAAA_geraldri-002E-ch_fa6806667ee298c61c6500282706afd6" {
  name    = "geraldri.ch"
  proxied = "true"
  ttl     = "1"
  type    = "AAAA"
  value   = "2606:50c0:8001::153"
  zone_id = "7d19aa4b3fa8b5bc91531ec6c6f80ec5"
}

resource "cloudflare_record" "tfer--A_geraldri-002E-ch_14ecb3464e4e396b3ae4dc691f91d285" {
  name    = "geraldri.ch"
  proxied = "true"
  ttl     = "1"
  type    = "A"
  value   = "185.199.109.153"
  zone_id = "7d19aa4b3fa8b5bc91531ec6c6f80ec5"
}

resource "cloudflare_record" "tfer--A_geraldri-002E-ch_182a97eb7855a69e2fe7cf60f3ba8217" {
  name    = "geraldri.ch"
  proxied = "true"
  ttl     = "1"
  type    = "A"
  value   = "185.199.111.153"
  zone_id = "7d19aa4b3fa8b5bc91531ec6c6f80ec5"
}

resource "cloudflare_record" "tfer--A_geraldri-002E-ch_4babfae7e4f0d84e175062c15836e833" {
  name    = "geraldri.ch"
  proxied = "true"
  ttl     = "1"
  type    = "A"
  value   = "185.199.108.153"
  zone_id = "7d19aa4b3fa8b5bc91531ec6c6f80ec5"
}

resource "cloudflare_record" "tfer--A_geraldri-002E-ch_baf23a3d2ad9faa2a48a90a6923ec0f8" {
  name    = "geraldri.ch"
  proxied = "true"
  ttl     = "1"
  type    = "A"
  value   = "185.199.110.153"
  zone_id = "7d19aa4b3fa8b5bc91531ec6c6f80ec5"
}

resource "cloudflare_record" "tfer--CNAME_geraldri-002E-ch_57debc471f22dd98e6a9ef26e020db4f" {
  name    = "projects.geraldri.ch"
  proxied = "true"
  ttl     = "1"
  type    = "CNAME"
  value   = "geraldri.ch"
  zone_id = "7d19aa4b3fa8b5bc91531ec6c6f80ec5"
}

resource "cloudflare_record" "tfer--CNAME_geraldri-002E-ch_e0572b0d7bfdc3af2f2038703a91a4e6" {
  name    = "www.geraldri.ch"
  proxied = "true"
  ttl     = "1"
  type    = "CNAME"
  value   = "newsroomdev.github.io"
  zone_id = "7d19aa4b3fa8b5bc91531ec6c6f80ec5"
}

resource "cloudflare_record" "tfer--TXT_geraldri-002E-ch_6aeb89d4200428a6533385a5ad226620" {
  name    = "_github-pages-challenge-newsroomdev.geraldri.ch"
  proxied = "false"
  ttl     = "1"
  type    = "TXT"
  value   = "51168336464ed1d6b7ffe126a1a57e"
  zone_id = "7d19aa4b3fa8b5bc91531ec6c6f80ec5"
}

resource "cloudflare_zone" "tfer--geraldri-002E-ch" {
  paused = "false"
  plan   = "free"
  type   = "full"
  zone   = "geraldri.ch"
}
