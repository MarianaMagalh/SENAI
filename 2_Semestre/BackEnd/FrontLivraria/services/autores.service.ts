// declara a classe como injetavel, para as infos irem para a pagina
import { Injectable, inject } from "@angular/core";
import { HttpClient } from "@angular/common/http"; // realiza as requisições
import { Observable } from 'rxjs'; // retorna os erros
import { Autor } from "../models/autor";
import { environment } from "../environenment/environenment";

// classe injetavel
@Injectable({providedIn: 'root'})
export class AutoresService{
    private http = inject(HttpClient) // get put push delete
    private base = environment.apiBase

    listar(): Observable<Autor[]>{
        const url = `${this.base}autores`
        return this.http.get<Autor[]>(url)
    }
}