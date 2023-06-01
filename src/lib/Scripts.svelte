<script lang="ts">
	import { onMount } from 'svelte';
	import Headroom from 'headroom.js';

	onMount(() => {
		const jq = window.$;
		const isMobile = {
			Android: () => navigator.userAgent.match(/Android/i),
			BlackBerry: () => navigator.userAgent.match(/BlackBerry/i),
			iOS: () => navigator.userAgent.match(/iPhone|iPod/i),
			Opera: () => navigator.userAgent.match(/Opera Mini/i),
			Windows: () => navigator.userAgent.match(/IEMobile/i),
			any: () =>
				isMobile.Android() ||
				isMobile.BlackBerry() ||
				isMobile.iOS() ||
				isMobile.Opera() ||
				isMobile.Windows()
		};

		// opacity change on scroll
		const isScrolledIntoView = (elem: Element) => {
			const docViewTop = jq(window).scrollTop();
			const docViewBottom = docViewTop + jq(window).height();
			const elemTop = jq(elem).offset()?.top || 0;
			const elemBottom = elemTop + jq(elem).height();
			return elemBottom <= docViewBottom && elemTop >= docViewTop;
		};

		function changeOpacity() {
			jq('div.item').each((_, elem) => {
				const $img = jq(elem);
				$img.css('opacity', isScrolledIntoView(elem) ? '1.0' : '0.3');
			});
		}

		jq(() => {
			if (!isMobile.any() && window.innerWidth >= 640) {
				changeOpacity();
				jq(window).scroll(changeOpacity);
			} else {
				const $imgs = jq('img');
				const firstImgs = $imgs.slice(0, 6);
				firstImgs.each((_, elem) => {
					const $img = jq(elem);
					const ext = $img.attr('src').endsWith('jpg') ? '.jpg' : '.png';
					const root = $img.attr('src').split(ext);
					$img.attr('src', `${root[0]}_s${ext}`);
				});
				const laziedImgs = $imgs.slice(6);
				laziedImgs.each((_, elem) => {
					const $img = jq(elem);
					if ($img.attr('data-src')) {
						const ext = $img.attr('data-src').endsWith('jpg') ? '.jpg' : '.png';
						const root = $img.attr('data-src').split(ext);
						$img.attr('data-src', `${root[0]}_s${ext}`);
					}
				});
			}
			jq('img').unveil();

			const headerElem = document.getElementById('page-header');
			if (headerElem) {
				const header = new Headroom(headerElem, {
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
