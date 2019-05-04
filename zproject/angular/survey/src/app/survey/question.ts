export interface IQuestion {
    id: number;
    survey:number;
    format: string;
    question: string;
    sequence: number;
    page: number;
    created: Date;
}