import pokeImage from "./images/bulbasaur.jpg"
import "./Showcase.css"

export default function ShowCase() {
    const favPokemon = "Bulbasaur"
    const pokeCharacteristics = {
        type: "Grass",
        move: "Vine Whip"
    }
    return (
        <div className="showcase-wrapper">
            <h1>{`${favPokemon}'s`} Showcase Component</h1>
            <h2>{`${favPokemon}'s type is ${pokeCharacteristics.type} and one of their many moves is ${pokeCharacteristics.move}` }</h2>
            <img 
                src={ pokeImage } 
                alt="pokemon-image"
                className="showcase-image"
                style={{ paddingRight: '10px' }} 
            />
        </div>
    )
}