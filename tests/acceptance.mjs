import assert from 'node:assert/strict';import fs from 'node:fs';import {validateBundle} from '../src/validator.js';
const read=n=>JSON.parse(fs.readFileSync(new URL(`../public/data/${n}.json`,import.meta.url)));
const [s,c,q,p]=['syllabus','concepts','questions','provenance'].map(read);const bundle={schemaVersion:s.schemaVersion,syllabusNodes:s.records,concepts:c.records,questions:q.records,provenanceRecords:p.records};
let r=validateBundle(bundle);assert.equal(r.valid,true);assert.deepEqual(r.counts,{syllabusNodes:1,concepts:1,questions:1,provenanceRecords:1});
r=validateBundle({...bundle,schemaVersion:'99.0.0'});assert.equal(r.valid,false);
r=validateBundle({...bundle,questions:[{...q.records[0],verificationStatus:'XYZ'}]});assert.equal(r.valid,false);
r=validateBundle({...bundle,questions:[{...q.records[0],primaryConceptId:'MISSING'}]});assert.equal(r.valid,false);
r=validateBundle({...bundle,concepts:[...c.records,c.records[0]]});assert.equal(r.valid,false);
console.log('Sprint 1 acceptance tests passed');