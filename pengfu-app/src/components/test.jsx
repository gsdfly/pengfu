import React from 'react'
import PropTypes from 'prop-types';

const Money = React.createContext(0);
//想要在生命周期里面获取context的时候，需要用函数组件将所需要用到的组件在包装一下

//如果多个组件需要用到上下文，可以抽离出一个高阶组件 及传入一个组件返回被处理的组件 感觉和修饰符相似

class Grandson extends React.Component {
    constructor(props){
        super(props)
    }
    componentDidMount(){
        console.log(this.props.value)
    }
    render(){
        return (<div>爷爷给了我{this.props.value}元</div>)
    }
}
const D2 = React.forwardRef((props, ref) => (
    <Money.Consumer>
        {value => (
            <Grandson {...props} value={value} ref={ref} />
        )}
    </Money.Consumer>
));
function W1(Component) {
    return function W2(props) {
        return (
            <Money.Consumer>
                {value=><Component {...props} value={value}/>}
            </Money.Consumer>
        )
    }
}

//refs转发，是因为在生命周期需要使用context时，需要将组件使用函数组件包裹，

const Dd = W1(Grandson);
//函数组件没有ref但是可以在函数组件内部使用ref

class Son extends React.Component{
    constructor(props){
        super(props)
    }
    componentDidMount(){
    console.log(this.r)
    }
    render(){
       return(
           <D2 ref={r=>{this.r = r}} />)
    }
}

class MyPerson extends React.Component {
    constructor(props){
        super(props);
        this.state = {
            value:500
        }
    }
    handleClick(){
        //模样已经成熟，心智还未成熟
        this.setState({
            value:600
        })
    }
    render() {
        return (
            <Money.Provider value={this.state.value}>
                <button onClick={()=>this.handleClick()}>改变</button>
                <Son/>
            </Money.Provider>
        )
    }
}
Son.propTypes = {
    money:PropTypes.number
}

export default MyPerson