import { moves } from "./data"
import PokeMoveCard from "./PokeMoveCard"

export default function PokeMoves() {

    return (
        <div>
            <h1>PokeMoves</h1>
            <ul>
                {moves.map(item => (
                    <PokeMoveCard key={ item.key } {...item}/>
                ))}:
            </ul>
        </div>
    );
}