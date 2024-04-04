export default function BaseStats({stats, clicker}) {


    return (
        <>
            <button 
                className="sp-stats"
                onClick={ clicker }
            >
                    Check Special State
            </button>
            <table>
                <tbody>
                    <tr>
                        <td>Hit Points</td>
                        <td>{stats.hp}</td>
                    </tr>
                    <tr>
                        <td>Attack</td>
                        <td>{stats.attack}</td>
                    </tr>
                    <tr>
                        <td>Defense</td>
                        <td>{stats.defense}</td>
                    </tr>
                    <tr>
                        <td>Speed</td>
                        <td>{stats.speed}</td>
                    </tr>
                </tbody>
            </table>
        </>
    );
}