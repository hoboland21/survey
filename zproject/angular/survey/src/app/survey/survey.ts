export interface ISurvey {
    id: number;
    name: string;
    requester: string;
    description: string;
    url: string;
    locked: boolean;
    created: Date;
}
