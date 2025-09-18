import { Injectable, signal } from "@angular/core";
import { HttpCliente } from "@angular/common/http";
import { Observable, tap } from " rxjs";
import { environment } from "../environenment/environenment";

type TokenPair = {access:string; refresh?: string}
const storage = {
    // get.item, set.item, delete.item
    // typeof - tipo interno, como local storage
    get: (k: string) => (typeof localStorage !== 'undefined' ? localStorage.getItem(k) : null) 
    set: (k: string, v: string) => {if(typeof localStorage !== 'undefined') localStorage.setItem(k, v)} 
}