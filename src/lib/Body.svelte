<script lang="ts">
	import 'lazysizes';
	import Nav from '$lib/Nav.svelte';
	import Row from '$lib/Row.svelte';
	import Serif from '$lib/Serif.svelte';
	import type { PageData } from '../routes/$types';
	import type { Contents } from './types';
	export let data: PageData;

	let content: Contents;
	if (data.body && 'content' in data.body) {
		content = data.body.content as Contents;
	}
</script>

<Nav />
<header class="sr-only">Hello there!</header>
<main class="rows">
	{#each content as row, index}
		<Row {row} {index} />
	{/each}
</main>
<footer>
	<Serif>
		<p class="footer">
			Created by Gerald Rich | <a href="https://github.com/newsroomdev/portfolio">Github Repo</a>
		</p>
	</Serif>
</footer>

<style lang="scss">
	@import './styles/variables';

	.rows {
		max-width: 1140px;
		margin: 0 0.25rem;

		@media (min-width: $breakpoint-lg) {
			margin: 0 auto;
			padding: 0 2rem;
		}
	}

	.footer {
		width: 100%;
		max-width: 1260px;
		font-size: 0.75rem;
		text-align: center;
		margin: 2rem auto 1rem;
		padding-top: 1rem;
		border-top: 1px solid #ccc;
	}

	.sr-only:not(:focus):not(:active) {
		clip: rect(0 0 0 0);
		clip-path: inset(50%);
		height: 1px;
		overflow: hidden;
		position: absolute;
		white-space: nowrap;
		width: 1px;
	}
</style>
