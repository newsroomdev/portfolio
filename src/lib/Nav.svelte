<script lang="ts">
	import { onMount } from 'svelte';
	import { base } from '$app/paths';
	import Serif from '$lib/Serif.svelte';
	import SansSerif from '$lib/SansSerif.svelte';

	$: scrolled = false;

	onMount(() => {
		const progressBar = document.getElementById('progress-bar');

		const updateScroll = () => {
			const scrollTop = window.pageYOffset || document.documentElement.scrollTop;
			const scrollHeight =
				document.documentElement.scrollHeight - document.documentElement.clientHeight;
			const scrollProgress = (scrollTop / scrollHeight) * 100;

			if (progressBar) progressBar.style.width = scrollProgress + '%';

			window.scrollY > 0 ? (scrolled = true) : (scrolled = false);
		};

		window.addEventListener('scroll', updateScroll);

		return () => {
			window.removeEventListener('scroll', updateScroll);
		};
	});
</script>

<nav id="page-headr" class="animated slide-down headroom--top">
	<h1 id="hed" class:scrolled>
		<Serif weight={400}>Gerald Rich</Serif>
	</h1>
	<SansSerif weight={400}>
		<div class="sub-nav" class:scrolled id="resume">
			<a target="_blank" rel="noopener" href="{base}/GeraldRichResume.pdf">Résumé</a>
		</div>
		<div class="sub-nav" class:scrolled>
			<a href="https://www.linkedin.com/in/geraldrich/">LinkedIn</a>
		</div>
	</SansSerif>
	<div id="progress-bar" />
</nav>

<style lang="scss">
	@import './styles/variables';

	#page-headr {
		position: sticky;
		top: 0;
		display: flex;
		justify-content: space-between;
		align-items: center;
		background-color: #fff;
		border-bottom: 1px solid #ccc;
		max-width: 1260px;
		width: 100%;
		margin: 0 auto;
		z-index: 1000;
	}

	#hed {
		font-size: 1.6rem; /* initial font size */
		transition: font-size 0.3s ease; /* transition effect */

		&.scrolled {
			font-size: 1.1rem;

			@media (min-width: $breakpoint-lg) {
				font-size: 1.2rem;
			} /* font size when scrolled */
		}

		@media (min-width: $breakpoint-mobile-md) {
			font-size: 1.8rem; /* initial font size */
		}

		@media (min-width: $breakpoint-mobile-lg) {
			font-size: 2rem;
		}
	}

	.sub-nav {
		display: inline-flex;
		gap: 1rem;
		transition: font-size 0.3s ease; /* transition effect */

		&.scrolled {
			font-size: 0.85rem;

			@media (min-width: $breakpoint-lg) {
				font-size: 0.9rem;
			}
		}

		&#resume {
			margin-right: 0;

			@media (min-width: $breakpoint-mobile-md) {
				margin-right: 0.2rem;
			}

			@media (min-width: $breakpoint-md) {
				margin-right: 0.5rem;
			}

			@media (min-width: $breakpoint-lg) {
				margin-right: 1rem;
			}
		}
	}

	#progress-bar {
		position: absolute;
		bottom: 0;
		left: 0;
		height: 1px;
		background: cornflowerblue;
		width: 0;
	}
</style>
