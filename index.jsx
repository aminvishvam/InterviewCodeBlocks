import react from "react"


const StarComponent = () => {
    return <>*</>
}

const parentComponent = () => {
    const startList = [1, 2, 3]

    startList.map(star => {
        return <><StarComponent /></>
    })

}