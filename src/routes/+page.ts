import archieml from 'archieml';
import type { PageLoad } from './$types';

export const load: PageLoad = async ({ fetch }) => {
	const res = await fetch(
		'https://docs.google.com/document/d/1k3sVL4rce_HlLFCp7lmnFvDvGNtasHmxIuGMDuzfpYM/export?format=txt'
	);
	const body = await res.text();
	const data = archieml.load(body);

	if (res.ok) {
		return { body: data };
	} else {
		return { status: res.status, error: new Error(`Could not load data`) };
	}
};
