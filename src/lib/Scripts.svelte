<script lang="ts">
	import { onMount } from 'svelte';
	import Headroom from "headroom.js";

	onMount(() => {
		const jq = window.$;
		var isMobile = {
			Android: function () {
				return navigator.userAgent.match(/Android/i);
			},
			BlackBerry: function () {
				return navigator.userAgent.match(/BlackBerry/i);
			},
			iOS: function () {
				return navigator.userAgent.match(/iPhone|iPod/i);
			},
			Opera: function () {
				return navigator.userAgent.match(/Opera Mini/i);
			},
			Windows: function () {
				return navigator.userAgent.match(/IEMobile/i);
			},
			any: function () {
				return (
					isMobile.Android() ||
					isMobile.BlackBerry() ||
					isMobile.iOS() ||
					isMobile.Opera() ||
					isMobile.Windows()
				);
			}
		};

		// opacity change on scroll

		function isScrolledIntoView(elem: Element) {
			var docViewTop = jq(window).scrollTop();
			var docViewBottom = docViewTop + jq(window).height();

			var elemTop = jq(elem).offset()?.top || 0;
			var elemBottom = elemTop + jq(elem).height();

			return elemBottom <= docViewBottom && elemTop >= docViewTop;
		}

		function chngeOpacity() {
			jq("div.item").each((_, elem) => {
				var img = jq(elem);
				if (isScrolledIntoView(elem)) {
					img.css('opacity', '1.0');
				} else {
					img.css('opacity', '0.3');
				}
			});
		}

		jq(function () {
			if (!isMobile.any() && window.innerWidth >= 640) {
				chngeOpacity();
				jq(window).scroll(chngeOpacity);
			} else {
				var $imgs = jq("img");
				var first_imgs = $imgs.slice(0, 6);
				jq(first_imgs).each((_, elem) => {
					var img = jq(elem);
					var ext = img.attr('src').endsWith('jpg') ? '.jpg' : '.png';
					var root = img.attr('src').split(ext);
					img.attr('src', `${root[0]}_s${ext}`);
				});
				var lazied_imgs = $imgs.slice(6);
				jq(lazied_imgs).each((_, elem) => {
					var img = jq(elem);
					if (img.attr('data-src')) {
						var ext = img.attr('data-src').endsWith('jpg') ? '.jpg' : '.png';
						var root = img.attr('data-src').split(ext);
						img.attr('data-src', `${root[0]}_s${ext}`);
					}
				});
			}
			jq("img").unveil();

			const hedElem = document.getElementById('page-headr')
			if (hedElem) {
				const header = new Headroom(hedElem, {
					tolerance: 5,
					offset: 205,
					classes: {
						initial: 'animated',
						pinned: 'slide-down',
						unpinned: 'slide-up'
					}
				});
				header.init();
			}
		});
	});
</script>
