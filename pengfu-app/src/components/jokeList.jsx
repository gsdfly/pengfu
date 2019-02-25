import React from 'react'
import JokeItem from './jokeItem'

class JokeList extends React.Component{
    constructor(){
        super();
        this.state = {
            pageIndex:1,
            pageSize:20,
            jokes:[],
            intersectionObserver:{},
            moreStyle:{
                display:'none',
            }
        }
    }
    componentDidMount(){
        // 开始观察
        // intersectionObserver.observe(document.getElementById('example'));
        // 停止观察
        // intersectionObserver.unobserve(element);
        // 关闭观察器
        // intersectionObserver.disconnect();
        var more = document.querySelector('.more');
        var intersectionObserver = new IntersectionObserver(function (entries) {
            // 如果不可见，就返回
            if (entries[0].intersectionRatio <= 0) return;
            this.nextPage();
            console.log('Loaded new items');
        }.bind(this));
        this.setState({
            intersectionObserver:intersectionObserver
        });
        intersectionObserver.observe(more);
        // document.querySelector('.jokeList').addEventListener('scroll', this.handleClick);
        fetch('http://proxy.litianyu.top/api?pageIndex='+this.state.pageIndex+"&pageSize="+this.state.pageSize,
        //     {
        //     method:'Get',
        //     headers: new Headers({
        //         // 'Accept': 'application/json', // 通过头指定，获取的数据类型是JSON
        //         // 'Content-Type':'application/json'
        //         'Content-Type': 'application/x-www-form-urlencoded'
        //     }),
        //     // body:JSON.stringify({"pageIndex":this.state.pageIndex,"pageSize":this.state.pageSize})
        // }
        ).then((res)=>res.json()).then((data)=>{
            console.log(data);
            this.setState({
                jokes:data.data
            })
        })
    }
    nextPage(){
        var nextPageIndex = this.state.pageIndex+1;
        this.setState({
            pageIndex:nextPageIndex
        })
        fetch('http://proxy.litianyu.top/api?pageIndex='+this.state.pageIndex+"&pageSize="+this.state.pageSize,
        ).then((res)=>res.json()).then((data)=>{
            console.log(data);
            if (data.data.length===0){
                this.state.intersectionObserver.disconnect();
            }
            var newDate = [...this.state.jokes,...data.data]
            this.setState({
                jokes:newDate
            })
        })
    }
    handleScroll(){
        if(JSON.stringify(this.state.moreStyle) != '{}'){
            this.setState({
                moreStyle:{}
            })
        }
    }
    render(){
        return <div className={'jokeList'} onScroll={()=>{this.handleScroll()}}>
            {this.state.jokes.map((value)=>{
                return <JokeItem key={value.id} jokeItem={value}></JokeItem>
            })}
            <div className={'more'} style={this.state.moreStyle}>加载更多</div>
        </div>
    }
}

export default JokeList