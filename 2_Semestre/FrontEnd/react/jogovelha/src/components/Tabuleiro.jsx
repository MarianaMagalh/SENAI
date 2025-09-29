import { useState } from "react";
import Quadrado from "./Quadrado";

export default function Tabuleiro() {
  // saber qual quadrado foi marcado
  const [quadrados, setQuadrados] = useState(Array(9).fill(null)); // 9 posições e vão iniciar vazios
  const [xProximo, setXProximo] = useState(true);
  function handleClick(i) {
    if (quadrados[i]) {
      return; // quando não for mais null, ele permanece o mesmo valor clicado inicialmente.
    }

    const nextQuadrado = quadrados.slice(); // criando um copia da constante
    // assim so reenderizando o quadrado e não a pagina toda

    if (xProximo) {
      nextQuadrado[i] = "X";
    } else {
      nextQuadrado[i] = "O";
    }

    setQuadrados(nextQuadrado); // atualizando a nova lista
    setXProximo(!xProximo); // aqui ele nega o xProximo, que vira false, e quando é negado novamente ele vira true, assim todo vez que clica X e O mudam
  }

  const venceu = vencedor(quadrados);
  let status;
  if (venceu) {
    status = "Vecendor eh: " + venceu;

  } else {
    status = "O Próximo jogador eh: " + (xProximo ? "X" : "O"); // ? como um if - operação ternario
  }

  // array function - obriga o sistema espera o click do usuario, evitando que renderize muitas vezes

  return (
    <>
      <main>
        <h1>Jogo da Velha</h1>
        <h2>{status}</h2>
        <div className="linha">
          <Quadrado className="quadrado"  value={quadrados[0]} onQuadrado={() => handleClick(0)} />
          <Quadrado className="quadrado"  value={quadrados[1]} onQuadrado={() => handleClick(1)} />
          <Quadrado className="quadrado"  value={quadrados[2]} onQuadrado={() => handleClick(2)} />
        </div>
        <div className="linha">
          <Quadrado className="quadrado"  value={quadrados[3]} onQuadrado={() => handleClick(3)} />
          <Quadrado className="quadrado"  value={quadrados[4]} onQuadrado={() => handleClick(4)} />
          <Quadrado className="quadrado"  value={quadrados[5]} onQuadrado={() => handleClick(5)} />
        </div>
        <div className="linha">
          <Quadrado className="quadrado"  value={quadrados[6]} onQuadrado={() => handleClick(6)} />
          <Quadrado className="quadrado"  value={quadrados[7]} onQuadrado={() => handleClick(7)} />
          <Quadrado className="quadrado"  value={quadrados[8]} onQuadrado={() => handleClick(8)} />
        </div>
      </main>
    </>
  );
}

function vencedor(quadrados) {
  const linhas = [
    [0, 1, 2],
    [3, 4, 5],
    [6, 7, 8],
    [0, 3, 6],
    [1, 4, 7],
    [2, 5, 8],
    [2, 4, 6],
    [0, 4, 8],
  ];

  for (let i = 0; i < linhas.length; i++) {
    const [a, b, c] = linhas[i];
    if (
      quadrados[a] &&
      quadrados[a] === quadrados[b] &&
      quadrados[a] === quadrados[c]
    ) {
      return quadrados[a];
    }
  }
  return null;
}
