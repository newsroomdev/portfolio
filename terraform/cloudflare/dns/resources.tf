resource "cloudflare_record" "tfer--AAAA_geraldri-002E-ch_7f7ba5718c45411293e0c9cf8faeccdc" {
  name    = "geraldri.ch"
  proxied = "true"
  ttl     = "1"
  type    = "AAAA"
  value   = "2606:50c0:8000::153"
  zone_id = "7d19aa4b3fa8b5bc91531ec6c6f80ec5"
}

resource "cloudflare_record" "tfer--A_geraldri-002E-ch_dae61abe2d0e0554f06b6363654ae3f8" {
  name    = "geraldri.ch"
  proxied = "true"
  ttl     = "1"
  type    = "A"
  value   = "185.199.108.153"
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

resource "cloudflare_zone" "tfer--geraldri-002E-ch" {
  paused = "false"
  plan   = "free"
  type   = "full"
  zone   = "geraldri.ch"
}
