// SINGLETON - Configurações Globais
// -----------------------------
class Config {
  constructor() {
    if (Config.instance) return Config.instance; // Se já existir uma instância, retorna a mesma
    this.settings = { theme: "light" }; // Configuração inicial (tema padrão)
    Config.instance = this; // Guarda a instância para reuso
  }

  set(key, value) { // Define um valor de configuração
    this.settings[key] = value;
  }

  get(key) { // Recupera um valor de configuração
    return this.settings[key];
  }
}

const config = new Config(); // Cria (ou reutiliza) a instância


// FACTORY - Criação de Usuários
// -----------------------------
class User {
  constructor(name) {
    this.name = name; // Nome do usuário
    this.role = "user"; // Papel padrão: usuário comum
  }
}

class PremiumUser extends User {
  constructor(name) {
    super(name); // Reutiliza o construtor da classe User
    this.role = "premium"; // Usuário premium tem papel diferente
  }
}

class UserFactory {
  create(type, name) { // Decide qual tipo de usuário criar
    switch (type) {
      case "premium": return new PremiumUser(name); // Cria usuário premium
      default: return new User(name); // Cria usuário comum
    }
  }
}

const userFactory = new UserFactory(); // Instancia a fábrica


// OBSERVER - Sistema de Notificações
// -----------------------------
class Subject {
  constructor() {
    this.observers = []; // Lista de observadores (quem vai receber notificações)
  }

  subscribe(observer) { // Permite adicionar um observador
    this.observers.push(observer);
  }

  notify(data) { // Envia uma notificação para todos os observadores
    this.observers.forEach(observer => observer.update(data));
  }
}

class Observer {
  constructor(name) {
    this.name = name; // Nome para identificar o observador
  }

  update(message) { // Função chamada quando há uma notificação
    console.log(`${this.name} recebeu notificação: ${message}`);
  }
}

const notifications = new Subject(); // Sistema central de notificações
// -----------------------------

// MODULE PATTERN - Autenticação
// -----------------------------
const AuthModule = (() => {
  let loggedUser = null; // Variável privada para armazenar usuário logado

  function login(user) {
    loggedUser = user; // Define quem está logado
    notifications.notify(`Usuário ${user.name} logou!`); // Notifica todos os observadores
  }

  function getUser() {
    return loggedUser; // Retorna o usuário logado
  }

  return { login, getUser }; // Expondo apenas o que é necessário
})();


// DECORATOR - Adicionando privilégios extras
// -----------------------------
function withAdminPrivileges(user) {
  return { 
    ...user, // Copia os dados do usuário
    role: "admin", // Altera o papel para admin
    deleteUsers: () => "Usuário deletado!" // Adiciona novo comportamento
  };
}