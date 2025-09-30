
export default function Quadrado({value, onQuadrado, disabled}){
    return(
        <button className="quadrado" onClick={onQuadrado} disabled={disabled}>
            {value}
        </button>
    );
}