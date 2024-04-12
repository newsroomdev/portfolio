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
	<h3>
		<SansSerif>Projects</SansSerif>
	</h3>
	{#each projects as project}
		<Project {project} />
	{/each}
</div>
