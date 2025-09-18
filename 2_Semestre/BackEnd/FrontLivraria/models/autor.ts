// sera uma tebala, semelhante ao do banco de dados
export interface Autor{
    id: number;
    name: string;
    last_name: string;
    birth_date?: string | null; // ela pode ser vazia, se existir ira ser numero
    nacionality?: string | null; 
    biography?: string | null;

}

export interface Editora{
    editora:string;
}