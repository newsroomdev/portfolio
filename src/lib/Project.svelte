<script lang="ts">
	import type { Project } from '$lib/types';
	import SansSerif from '$lib/SansSerif.svelte';
	import Serif from '$lib/Serif.svelte';
	export let project: Project;
	const { title, role, desc, img, link } = project;
</script>

<div class="sub-item">
	<div class="sub-desc">
		<h4>
			<SansSerif weight={400}>
				{#if link}
					<a class="title" href={link}>{title}</a>
				{:else}
					{title}
				{/if}
				<span>({role})</span>
			</SansSerif>
		</h4>
		{#if link}
			<a href={link}>
				<img src={img} loading="lazy" alt="" />
			</a>
		{:else}
			<img src={img} loading="lazy" alt="" />
		{/if}
		<Serif>
			<p>{desc}</p>
		</Serif>
	</div>
</div>

<style lang="scss">
	.sub-item {
		h4 {
			font-size: 1rem;
		}
		p {
			font-size: 0.75rem;
		}
	}
</style>
