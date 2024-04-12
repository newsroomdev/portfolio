<script lang="ts">
	import 'lazysizes';
	import Nav from '$lib/Nav.svelte';
	import Row from '$lib/Row.svelte';
	import content from '../data/content.json';
</script>

<Nav />
<div class="rows">
	{#each content as row}
		<Row {row} />
	{/each}
</div>

<style lang="scss">
	@import './styles/variables';

	.rows {
		max-width: 1140px;
		margin: 0 0.25rem;

		@media (min-width: $breakpoint-lg) {
			margin: 0 auto;
		}
	}
</style>
