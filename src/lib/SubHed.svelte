<script lang="ts">
	import type { Hed } from '$lib/types';
	import SansSerif from '$lib/SansSerif.svelte';
	import Serif from '$lib/Serif.svelte';
	export let hed: Hed;
	const { orgTitle, jobTitle, dates, guff, skills, link } = hed;
</script>

<div>
	<h2 class="h2">
		<SansSerif weight={400}>
			<a href={link}>{orgTitle}</a>
		</SansSerif>
		<SansSerif>
			<span class="job-desc">
				{jobTitle}
				<br />
				({dates})
			</span>
		</SansSerif>
	</h2>
	<div class="guff">
		<Serif>
			<div>{guff}</div>
			<div class="description">
				Skills: {skills.join(', ')}
			</div>
		</Serif>
	</div>
</div>

<style lang="scss">
	.h2 {
		font-size: 1.25rem;
	}

	.job-desc {
		display: block;
		font-size: 0.85rem;
	}

	.guff {
		font-size: 0.85rem;
	}

	.description {
		margin: 0.5rem 0;
	}
</style>
