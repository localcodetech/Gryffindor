
const url ="";
const apiKey = "OabZHcZFPO6cG0PjXlu3KoSeTzs3oLpqkp5rtdXYBfVmWAaRgnkyIu6wFShjE5W9"


async function Fetchdata (){
    const res = await fetch(url,
        {
            method: "GET",
            headers: {
                "Content-Type" : "application/json",
                "Accept": 'application/json',
                'X-Api-Key': apiKey,
                'X-Api-Host': 
            }
        }
    )
}