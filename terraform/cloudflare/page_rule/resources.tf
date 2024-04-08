# redirect old projects dot subdomain to root domain
resource "cloudflare_page_rule" "tfer--016f7506bf663401457b235c52990149" {
  actions {
    always_use_https    = "false"
    disable_apps        = "false"
    disable_performance = "false"
    disable_railgun     = "false"
    disable_security    = "false"
    edge_cache_ttl      = "0"

    forwarding_url {
      status_code = "301"
      url         = "https://geraldri.ch"
    }
  }

  priority = "3"
  status   = "active"
  target   = "projects.geraldri.ch/"
  zone_id  = "7d19aa4b3fa8b5bc91531ec6c6f80ec5"
}

resource "cloudflare_page_rule" "tfer--7a0b2cb4c96ec02895df816bd807ec28" {
  actions {
    always_use_https    = "false"
    disable_apps        = "false"
    disable_performance = "false"
    disable_railgun     = "false"
    disable_security    = "false"
    edge_cache_ttl      = "0"

    forwarding_url {
      status_code = "301"
      url         = "https://geraldri.ch"
    }
  }

  priority = "1"
  status   = "active"
  target   = "http://projects.geraldri.ch/portfolio"
  zone_id  = "7d19aa4b3fa8b5bc91531ec6c6f80ec5"
}

resource "cloudflare_page_rule" "tfer--972d0f21236580e4715b8e4c7c8cd8ad" {
  actions {
    always_use_https    = "false"
    disable_apps        = "false"
    disable_performance = "false"
    disable_railgun     = "false"
    disable_security    = "false"
    edge_cache_ttl      = "0"

    forwarding_url {
      status_code = "301"
      url         = "https://geraldri.ch"
    }
  }

  priority = "2"
  status   = "active"
  target   = "https://projects.geraldri.ch/portfolio"
  zone_id  = "7d19aa4b3fa8b5bc91531ec6c6f80ec5"
}
