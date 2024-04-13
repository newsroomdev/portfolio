<script lang="ts">
	import type { Hed } from '$lib/types';
	import SansSerif from '$lib/SansSerif.svelte';
	import Serif from '$lib/Serif.svelte';
	export let hed: Hed;
</script>

<div class="sub-hed">
	<h2 class="h2">
		<SansSerif weight={400}>
			{#if hed.link}
				<a href={hed.link}>{hed.orgTitle}</a>
			{:else}
				{hed.orgTitle}
			{/if}
		</SansSerif>
		<SansSerif>
			<span class="job-desc">
				<span class="job-title">{hed.jobTitle}</span>
				<br />
				<span class="dates">({hed.dates})</span>
			</span>
		</SansSerif>
	</h2>
	<div class="guff">
		<Serif>
			<div>{hed.guff}</div>
			<div class="description">
				Skills: {hed.skills.join(', ')}
			</div>
		</Serif>
	</div>
</div>

<style lang="scss">
	@import './styles/variables';
	.h2 {
		font-size: 1.25rem;
		margin-top: 1em;
	}

	.job-desc {
		display: block;
		font-size: 0.85rem;
	}

	.guff {
		font-size: 0.9rem;
	}

	.description {
		margin: 0.5rem 0;
	}

	@media (min-width: $breakpoint-xl) {
		.sub-hed {
			width: 100%;
			max-width: $breakpoint-mobile-md;
		}
	}
</style>
