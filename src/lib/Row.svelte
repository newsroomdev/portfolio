<script lang="ts">
	import type { Row } from '$lib/types';
	import SubHed from '$lib/SubHed.svelte';
	import Project from '$lib/Project.svelte';
	import SansSerif from './SansSerif.svelte';

	export let row: Row;
	export let index: number;
	const single = row.projects.length === 1;
</script>

<div class="row" class:single>
	<SubHed hed={row.hed} />
	<div>
		<h3>
			<SansSerif>Projects</SansSerif>
		</h3>
		<div class="projects">
			{#each row.projects as project}
				<Project {project} {index} />
			{/each}
		</div>
	</div>
</div>

<style lang="scss">
	@import './styles/variables';
	h3 {
		margin-bottom: 0;
		margin-top: 1em;
	}
	.projects {
		display: flex;
		flex-direction: column;
		column-gap: 1.5rem;
		align-items: center;
		justify-content: center;

		@media (min-width: $breakpoint-md) {
			flex-direction: row;
			justify-content: space-between;
		}

		@media (min-width: $breakpoint-lg) {
			justify-content: start;
			column-gap: 2rem;
			align-items: start;
		}
	}

	@media (min-width: $breakpoint-xl) {
		.row {
			display: flex;
			justify-content: space-between;
			column-gap: 5rem;
			align-items: center;
		}

		.single {
			justify-content: start;
		}
	}
</style>
