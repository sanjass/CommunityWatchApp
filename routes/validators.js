const express = require('express');

const Neighborhoods = require('../models/Neighborhoods');


// const Shorts = require('../models/Shorts');
// const Users = require('../models/Users');

// ------------------------------ AUTH

// const ensureUserNotLoggedIn = function(req, res, next) {
//   if (req.session.uid) {
//     res.status(400).json({ error: "You are signed in!" }).end();
//     return;
//   }
//   next();
// };

// const ensureUserLoggedIn = function(req, res, next) {
//   if (!req.session.uid) {
//     res.status(401).json({ error: "Must be signed in!" }).end();
//     return;
//   }
//   next();
// };

// // ------------------------------ BODY

// const ensureValidUsernameInBody = function(req, res, next) {
//   if (!req.body.username) {
//     res.status(400).json({ error: "You must specify a valid username in the body" }).end();
//     return;
//   }
//   next();
// };


// const ensureValidShortUrlInBody = function(req, res, next) {
//   if (!req.body.url) {
//     res.status(400).json({ error: "You must specify a valid short URL in the body" }).end();
//     return;
//   }
//   next();
// };

// // ------------------------------ AUTH

// const ensureValidShortNameParam = function(req, res, next) {
//   if (!req.params.name) {
//     res.status(400).json({ error: "You must specify the name of a short as a parameter" }).end();
//     return;
//   }
//   next();
// };


const ensureValidNeighborhoodIdInBody = function(req, res, next) {
  if (!req.body.neighborhoodId) {
    res.status(400).json({ error: "You must specify a valid neighborhood id in the body" }).end();
    return;
  }
  next();
};

module.exports = {

  ensureValidNeighborhoodIdInBody,
};