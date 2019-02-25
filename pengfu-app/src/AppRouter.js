import React from "react";
import { BrowserRouter as Router, Route, Link,Switch,Redirect } from "react-router-dom";

const Index = () => <h2>Home</h2>;
const About = (props) => <h2>About{props.extra}</h2>;
// const Users = () => <h2>Users</h2>;
const Topic = ({ match }) => <h3>Requested Param: {match.params.id}</h3>;
const Topics = ({ match }) => (
    <div>
        <h2>Topics</h2>

        <ul>
            <li>
                <Link to={`${match.url}/components`}>Components</Link>
            </li>
            <li>
                <Link to={`${match.url}/props-v-state`}>Props v. State</Link>
            </li>
        </ul>

        <Route path={`${match.path}/:id`} component={Topic} />
        <Route
            exact
            path={match.path}
            render={() => <h3>Please select a topic.</h3>}
        />
    </div>
);

const Home = () => <div>Home</div>;

const App = () => {
    const someVariable = 'dddd';

    return (
        <Router>
        <div>
                <ul>
                    <li>
                        <Link to="/">Home</Link>
                    </li>
                    <li>
                        <Link to="/about">ddd</Link>
                    </li>
                </ul>
        <Switch>
            {/* these are good */}
            <Route exact path="/" component={Home} />
            <Route
                path="/about"
                render={props => <About {...props} extra={someVariable} />}
            />
            {/* do not do this */}
            {/*<Route*/}
                {/*path="/contact"*/}
                {/*component={props => <Contact {...props} extra={someVariable} />}*/}
            {/*/>*/}
        </Switch>
            {/*<Redirect to="/about" />*/}
        </div>
        </Router>

    );
};

fetch('http://proxy.litianyu.top/api', {
    method: 'get',
})

const AppRouter = () => (
    <Router>
        <div>
            <nav>
                <ul>
                    <li>
                        <Link to="/">Home</Link>
                    </li>
                    <li>
                        <Link to="/about">About</Link>
                    </li>
                    <li>
                        <Link to="/Topics">Topics</Link>
                    </li>
                    <li>
                        <Link to="/dd">dd</Link>
                    </li>
                </ul>
            </nav>
            <Switch>
                <Route exact path="/" component={Index} />
                <Route path="/about" component={About} />
                <Route path="/Topics" component={Topics} />
                {/* when none of the above match, <NoMatch> will be rendered */}
                <Route component={Index} />
            </Switch>
            {/*<Route path="/" exact component={Index} />*/}
            {/*<Route path="/about" component={About} />*/}
            {/*<Route path="/Topics" component={Topics} />*/}
        </div>
    </Router>
);

export default App;