/**
 * Sample React Native App
 * https://github.com/facebook/react-native
 *
 * @format
 * @flow
 */

import React, {Fragment} from 'react';

import { mapping, light as lightTheme } from '@eva-design/eva';
import { ApplicationProvider, Layout } from 'react-native-ui-kitten';
import { HomeScreen } from './HomeScreen/HomeScreen'
import { SignInForm3 } from './signInForm3/signInForm3.component'

const App = () => (
  <ApplicationProvider
    mapping={mapping}
    theme={lightTheme}>
    <SignInForm3/>
  </ApplicationProvider>
);

export default App;
