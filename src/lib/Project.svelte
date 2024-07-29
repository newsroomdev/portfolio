<script lang="ts">
	import type { Project } from '$lib/types';
	import SansSerif from '$lib/SansSerif.svelte';
	import Serif from '$lib/Serif.svelte';
	import Img from '$lib/Img.svelte';

	export let project: Project;
	export let index: number;
</script>

<div class="sub-item">
	<h4>
		<SansSerif weight={400}>
			<span style="font-style: italic">
				{#if project.link}
					<a class="title" href={project.link}>{project.title}</a>
				{:else}
					{project.title}
				{/if}
			</span>
			{#if project.role}
				<span class="role">({project.role})</span>
			{/if}
		</SansSerif>
	</h4>
	{#if project.link && project.img}
		<a href={project.link}>
			<Img img={project.img} alt={project.title} loading={index === 0 ? 'eager' : 'lazy'} />
		</a>
	{:else if project.img}
		<Img img={project.img} alt={project.title} loading={index === 0 ? 'eager' : 'lazy'} />
	{/if}
	<Serif>
		<p>{@html project.desc}</p>
	</Serif>
</div>

<style lang="scss">
	@import './styles/variables.scss';
	.sub-item {
		display: flex;
		flex-direction: column;
		width: 100%;

		@media (min-width: $breakpoint-md) {
			width: 50%;
			min-width: 300px;
			margin: 0 auto;
		}

		@media (min-width: $breakpoint-xl) {
			width: 100%;
			max-width: $breakpoint-mobile-sm;
		}

		h4 {
			font-size: 1rem;
			margin-top: 0.2rem;

			@media (min-width: $breakpoint-md) {
				text-align: center;
			}

			@media (min-width: $breakpoint-lg) {
				text-align: left;
			}

			.role {
				font-weight: 200;
				font-size: 0.9rem;
			}
		}

		p {
			font-size: 0.8rem;
			color: $gray-color;
		}
	}
</style>
