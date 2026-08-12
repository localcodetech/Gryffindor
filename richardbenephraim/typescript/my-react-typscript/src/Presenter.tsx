
interface presenterprops{
    name?: string
    title?: string
    age?:number
    visible?:boolean
    

}


const Presenter = (props:presenterprops)=>{

    return (
        <div>
{props.name}
        </div>
    )
};

export default  Presenter;