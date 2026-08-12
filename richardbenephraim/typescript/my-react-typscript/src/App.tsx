import  
{useRef, useState} from "react"
import "./App.css"
import Presenter from "./Presenter";

const App = ()=>{

  const ref = useRef(null)
  const [state, setState] = useState<number | string>()

  return (
      <div ref={ref}>
<Presenter  name="kwesi"/>
      </div>

  )
};

export default App;