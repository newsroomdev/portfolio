<script lang="ts">
	import Head from '$lib/Head.svelte';
	import Body from '$lib/Body.svelte';
	import '$lib/styles/global.scss';
	import type { PageData } from './$types';

	export let data: PageData;
</script>

<div class="wrapper">
	<Head />
	<Body {data} />
</div>

<style lang="scss">
	@import '../lib/styles/variables';

	:global(html, body) {
		margin: 0;
		font-size: 16px;
		line-height: 1.3;
	}

	.wrapper {
		display: flex;
		flex-direction: column;
		margin: 0 1rem;

		@media (min-width: $breakpoint-lg) {
			margin: 0 2.5rem;
		}
	}
</style>
