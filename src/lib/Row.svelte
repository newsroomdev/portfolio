<script lang="ts">
	import type { Row } from '$lib/types';
	import SubHed from '$lib/SubHed.svelte';
	import Project from '$lib/Project.svelte';
	import SansSerif from './SansSerif.svelte';

	export let row: Row;

	const { hed, projects } = row;
</script>

<div class="row">
	<SubHed {hed} />
	<div>
		<h3>
			<SansSerif>Projects</SansSerif>
		</h3>
		<div class="projects">
			{#each projects as project}
				<Project {project} />
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
		column-gap: 1rem;
		align-items: center;
		justify-content: center;

		@media (min-width: $breakpoint-md) {
			flex-direction: row;
		}
	}

	@media (min-width: $breakpoint-xl) {
		.row {
			display: flex;
			justify-content: space-between;
			column-gap: 5rem;
		}
	}
</style>
