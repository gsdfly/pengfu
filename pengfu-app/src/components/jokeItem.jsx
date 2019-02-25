import React from 'react'

class JokeItem extends React.Component{
    render(){
        return <div className={'jokeitem'}>
            {this.props.jokeItem.name ? <p>{this.props.jokeItem.name}</p>:''}
            {this.props.jokeItem.title ? <h3>{this.props.jokeItem.title}</h3>:''}
            {this.props.jokeItem.img ? <img src={this.props.jokeItem.img} alt=""/> : ''}
            {this.props.jokeItem.content ? <p>{this.props.jokeItem.content}</p> : ''}
        </div>
    }
}

export default JokeItem