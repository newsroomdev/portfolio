<script lang="ts">
	import 'lazysizes';
	import Nav from '$lib/Nav.svelte';
	import Row from '$lib/Row.svelte';
	import Serif from '$lib/Serif.svelte';
	import content from '../data/content.json';
</script>

<Nav />
<div class="rows">
	{#each content as row}
		<Row {row} />
	{/each}
</div>
<footer>
	<Serif>
		<p class="footer">
			Created by Gerald Rich | <a href="https://github.com/newsroomdev/portfolio">View Source</a>
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
		font-size: 0.85rem;
		text-align: center;
		margin: 2rem auto 1rem;
		padding-top: 1rem;
		border-top: 1px solid #ccc;
	}
</style>
