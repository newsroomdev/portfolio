export interface Row {
	hed: Hed;
	projects: Project[];
}

export interface Hed {
	orgTitle: string;
	jobTitle: string;
	link?: string;
	dates: string;
	guff: string;
	skills: string[];
}

export interface Project {
	title: string;
	role: string;
	desc: string;
	img: string;
	link?: string;
}

// Since the JSON is an array of Content objects
export type Contents = Row[];
